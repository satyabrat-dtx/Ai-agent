# DB2ADMIN.WFMCUSTOOPTIONCPY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `no_primary_key`
- **Columns**: 8
- **Primary key**: _none declared_
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 115722

> No primary key declared; rows are not uniquely addressable by the schema.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PLYWFMINTEGRATIONCODE` | CHAR(20) |  |  |  |  |
| 2 | `WFMBASEURI` | VARCHAR(250) | NOT NULL |  |  |  |
| 3 | `WFMID` | CHAR(65) | NOT NULL |  |  |  |
| 4 | `WFMPWD` | CHAR(20) | NOT NULL |  |  |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `WFMHISTORYBASEURI` | VARCHAR(250) | NOT NULL |  |  |  |
| 7 | `WFMOAUTHBASEURI` | VARCHAR(250) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PLYWFMINTEGRATIONCODE,
       t.WFMBASEURI,
       t.WFMID,
       t.WFMPWD,
       t.ABSUNIQUEID,
       t.WFMHISTORYBASEURI,
       t.WFMOAUTHBASEURI
FROM   DB2ADMIN.WFMCUSTOOPTIONCPY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
