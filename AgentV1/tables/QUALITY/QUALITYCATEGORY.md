# DB2ADMIN.QUALITYCATEGORY

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123236

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(2) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 3 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 4 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 5 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 6 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 7 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYCATEGORY.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `QUALITYCATEGORY_DETAIL` | [`QUALITYCATEGORYDETAIL`](../QUALITY/QUALITYCATEGORYDETAIL.md) | `QUALITYCATEGORYCOMPANYCODE`, `QUALITYCATEGORYCODE` | `QUALITYCATEGORYDETAIL.QUALITYCATEGORYCOMPANYCODE = QUALITYCATEGORY.COMPANYCODE AND QUALITYCATEGORYDETAIL.QUALITYCATEGORYCODE = QUALITYCATEGORY.CODE` |
| `QUALITYCATEGORY_QUALITYCATEGORY` | [`RG1TRANSACTION`](../QUALITY/RG1TRANSACTION.md) | `COMPANYCODE`, `QUALITYCATEGORYCODE` | `RG1TRANSACTION.COMPANYCODE = QUALITYCATEGORY.COMPANYCODE AND RG1TRANSACTION.QUALITYCATEGORYCODE = QUALITYCATEGORY.CODE` |

## Indexes

- `QUALITYCATEGORYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.QUALITYCATEGORY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
