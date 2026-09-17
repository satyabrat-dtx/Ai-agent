# DB2ADMIN.USAOPENBALANCE

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`, `ORDPRNCUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 88414

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDPRNCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 3 | `OPENBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 4 | `CREDITMODECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USAOPENBALANCE.COMPANYCODE = COMPANY.CODE` |
| `USACREDITCHECKMODE_CREDITMODE` | `CREDITMODECODE` | [`USACREDITCHECKMODE`](../LOCALIZATION/USACREDITCHECKMODE.md) | `CODE` | RESTRICT | `USAOPENBALANCE.CREDITMODECODE = USACREDITCHECKMODE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USAOPENBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDPRNCUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.OPENBALANCE,
       t.CREDITMODECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USAOPENBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
