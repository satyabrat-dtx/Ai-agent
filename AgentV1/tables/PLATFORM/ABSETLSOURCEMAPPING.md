# DB2ADMIN.ABSETLSOURCEMAPPING

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `ABSETLSOURCESOURCEID`, `TARGETFIELD`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93762

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSETLSOURCESOURCEID` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TARGETFIELD` | CHAR(65) | NOT NULL | PK | primary_key |  |
| 2 | `MAPPINGTYPE` | INTEGER | NOT NULL |  |  |  |
| 3 | `SOURCEFIELD` | CHAR(65) |  |  |  |  |
| 4 | `DEFAULTVALUE` | CHAR(65) |  |  |  |  |
| 5 | `NESTEDSOURCESOURCEID` | CHAR(30) |  | FK | foreign_key |  |
| 6 | `PLYMAPPINGCODE` | CHAR(20) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSETLSOURCE_MAPPING` | `ABSETLSOURCESOURCEID` | [`ABSETLSOURCE`](../PLATFORM/ABSETLSOURCE.md) | `SOURCEID` | RESTRICT | `ABSETLSOURCEMAPPING.ABSETLSOURCESOURCEID = ABSETLSOURCE.SOURCEID` |
| `ABSETLSOURCE_NESTEDSOURCE` | `NESTEDSOURCESOURCEID` | [`ABSETLSOURCE`](../PLATFORM/ABSETLSOURCE.md) | `SOURCEID` | RESTRICT | `ABSETLSOURCEMAPPING.NESTEDSOURCESOURCEID = ABSETLSOURCE.SOURCEID` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSETLSOURCEMAPPING_LINKS` | [`ABSETLSOURCEMAPLINK`](../PLATFORM/ABSETLSOURCEMAPLINK.md) | `ABSETLSOURCESOURCEID`, `ABSETLSOURCEMAPPINGTARGETFIELD` | `ABSETLSOURCEMAPLINK.ABSETLSOURCESOURCEID = ABSETLSOURCEMAPPING.ABSETLSOURCESOURCEID AND ABSETLSOURCEMAPLINK.ABSETLSOURCEMAPPINGTARGETFIELD = ABSETLSOURCEMAPPING.TARGETFIELD` |

## Indexes

- `ABSETLSOURCEMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSETLSOURCESOURCEID,
       t.TARGETFIELD,
       t.MAPPINGTYPE,
       t.SOURCEFIELD,
       t.DEFAULTVALUE,
       t.NESTEDSOURCESOURCEID,
       t.PLYMAPPINGCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ABSETLSOURCEMAPPING t
FETCH FIRST 100 ROWS ONLY;
```
