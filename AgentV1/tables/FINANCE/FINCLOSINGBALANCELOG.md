# DB2ADMIN.FINCLOSINGBALANCELOG

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 179107

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `GLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `GLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 6 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 7 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `CLOSINGBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 15 | `OPNDOCCLOSINGAMT` | DECIMAL(18,5) |  |  |  |  |
| 16 | `REMARKS` | CHAR(30) |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `GLMASTER_GL` | `GLCOMPANYCODE`, `GLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINCLOSINGBALANCELOG.GLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINCLOSINGBALANCELOG.GLCODE = GLMASTER.CODE` |
| `ORDERPARTNER_SL` | `COMPANYCODE`, `SLCUSTOMERSUPPLIERTYPE`, `SLCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `FINCLOSINGBALANCELOG.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND FINCLOSINGBALANCELOG.SLCUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND FINCLOSINGBALANCELOG.SLCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCLOSINGBALANCELOGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.BUSINESSUNITCODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.SLCUSTOMERSUPPLIERTYPE,
       t.SLCUSTOMERSUPPLIERCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FINCLOSINGBALANCELOG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
