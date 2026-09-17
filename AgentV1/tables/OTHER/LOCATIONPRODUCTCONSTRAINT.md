# DB2ADMIN.LOCATIONPRODUCTCONSTRAINT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `PRODUCTITEMTYPECODE`, `PRODUCTSUBCODE01`, `PRODUCTSUBCODE02`, `PRODUCTSUBCODE03`, `PRODUCTSUBCODE04`, `PRODUCTSUBCODE05`, `PRODUCTSUBCODE06`, `PRODUCTSUBCODE07`, `PRODUCTSUBCODE08`, `PRODUCTSUBCODE09`, `PRODUCTSUBCODE10`, `LOCTYPESTANDARDGROUPTYPECODE`, `LOCATIONTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13555

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `PRODUCTSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 3 | `PRODUCTSUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `PRODUCTSUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 5 | `PRODUCTSUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `PRODUCTSUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `PRODUCTSUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 8 | `PRODUCTSUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 9 | `PRODUCTSUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 10 | `PRODUCTSUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 11 | `PRODUCTSUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `LOCTYPESTANDARDGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 13 | `LOCATIONTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 14 | `UNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 21 | `PRODUCTITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 22 | `PRODUCTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 23 | `LOCTYPESTDGRPTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LOCATIONPRODUCTCONSTRAINT.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_UNITOFMEASURE` | `UNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `LOCATIONPRODUCTCONSTRAINT.UNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LOCATIONPRODUCTCONSTRAINTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTITEMTYPECODE,
       t.PRODUCTSUBCODE01,
       t.PRODUCTSUBCODE02,
       t.PRODUCTSUBCODE03,
       t.PRODUCTSUBCODE04,
       t.PRODUCTSUBCODE05,
       t.PRODUCTSUBCODE06,
       t.PRODUCTSUBCODE07,
       t.PRODUCTSUBCODE08,
       t.PRODUCTSUBCODE09,
       t.PRODUCTSUBCODE10
FROM   DB2ADMIN.LOCATIONPRODUCTCONSTRAINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
