# DB2ADMIN.FINCSFI8

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `URSRID`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103864

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(8) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(8) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `URSRID` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 3 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 4 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 5 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 6 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINCSFI8_URSRREP` | [`FINCSFI8REPORTS`](../FINANCE/FINCSFI8REPORTS.md) | `FINCSFI8COMPANYCODE`, `FINCSFI8DIVISIONCODE`, `FINCSFI8URSRID` | `FINCSFI8REPORTS.FINCSFI8COMPANYCODE = FINCSFI8.COMPANYCODE AND FINCSFI8REPORTS.FINCSFI8DIVISIONCODE = FINCSFI8.DIVISIONCODE AND FINCSFI8REPORTS.FINCSFI8URSRID = FINCSFI8.URSRID` |

## Indexes

- `FINCSFI8UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.URSRID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINCSFI8 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
