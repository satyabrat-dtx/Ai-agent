# DB2ADMIN.ABSETLSOURCE

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `SOURCEID`
- **FK degree**: referenced by 2 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93676

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SOURCEID` | CHAR(30) | NOT NULL | PK | primary_key |  |
| 1 | `DESCRIPTION` | VARCHAR(250) | NOT NULL |  | description |  |
| 2 | `CONNECTIONNAME` | CHAR(100) | NOT NULL |  |  |  |
| 3 | `ETLSOURCETABLE` | CHAR(128) | NOT NULL |  |  |  |
| 4 | `ETLSOURCETABLEUNIQUEID` | CHAR(128) | NOT NULL |  |  |  |
| 5 | `ETLLASTREAD` | BIGINT | NOT NULL |  |  |  |
| 6 | `ETLSELECTPATTERN` | VARCHAR(2000) |  |  |  |  |
| 7 | `ETLTARGETBEANPATH` | VARCHAR(50) |  |  |  |  |
| 8 | `ETLTARGETBEANNAME` | VARCHAR(54) |  |  |  |  |
| 9 | `ETLTARGETASYNCIMPORT` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ETLTARGETEJBSESSIONPATH` | VARCHAR(50) |  |  |  |  |
| 11 | `ETLTARGETEJBSESSIONNAME` | VARCHAR(54) |  |  |  |  |
| 12 | `ETLTARGETEJBMETHOD` | CHAR(50) | NOT NULL |  |  |  |
| 13 | `PLYMAPPINGCODE` | CHAR(20) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSETLSOURCE_MAPPING` | [`ABSETLSOURCEMAPPING`](../PLATFORM/ABSETLSOURCEMAPPING.md) | `ABSETLSOURCESOURCEID` | `ABSETLSOURCEMAPPING.ABSETLSOURCESOURCEID = ABSETLSOURCE.SOURCEID` |
| `ABSETLSOURCE_NESTEDSOURCE` | [`ABSETLSOURCEMAPPING`](../PLATFORM/ABSETLSOURCEMAPPING.md) | `NESTEDSOURCESOURCEID` | `ABSETLSOURCEMAPPING.NESTEDSOURCESOURCEID = ABSETLSOURCE.SOURCEID` |

## Indexes

- `ABSETLSOURCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SOURCEID,
       t.DESCRIPTION,
       t.CONNECTIONNAME,
       t.ETLSOURCETABLE,
       t.ETLSOURCETABLEUNIQUEID,
       t.ETLLASTREAD,
       t.ETLSELECTPATTERN,
       t.ETLTARGETBEANPATH,
       t.ETLTARGETBEANNAME,
       t.ETLTARGETASYNCIMPORT,
       t.ETLTARGETEJBSESSIONPATH,
       t.ETLTARGETEJBSESSIONNAME
FROM   DB2ADMIN.ABSETLSOURCE t
FETCH FIRST 100 ROWS ONLY;
```
