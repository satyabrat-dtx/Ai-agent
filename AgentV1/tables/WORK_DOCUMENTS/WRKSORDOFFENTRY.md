# DB2ADMIN.WRKSORDOFFENTRY

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205495

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATERECEIPTENTRY` | SMALLINT | NOT NULL |  |  |  |
| 2 | `ENTRYLOGWHS` | CHAR(8) |  |  |  |  |
| 3 | `LOCATION` | CHAR(10) |  |  |  |  |
| 4 | `PHYWHS` | CHAR(8) |  |  |  |  |
| 5 | `ZONE` | CHAR(3) |  |  |  |  |
| 6 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 7 | `ELEMENTCODE` | CHAR(10) |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSORDOFFENTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATERECEIPTENTRY,
       t.ENTRYLOGWHS,
       t.LOCATION,
       t.PHYWHS,
       t.ZONE,
       t.CREATIONTIMESTAMP,
       t.ELEMENTCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WRKSORDOFFENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
