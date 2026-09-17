# DB2ADMIN.ABSMAILBOXVEVENT

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `ABSMAILBOXMAILIDENTIFIER`, `PROPKEY`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 117837

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ABSMAILBOXMAILIDENTIFIER` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PROPKEY` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `ORGANIZERASCHAIR` | SMALLINT | NOT NULL |  |  |  |
| 3 | `DTSTARTDATE` | DATE |  |  |  |  |
| 4 | `DTSTARTDATEUTC` | TIMESTAMP |  |  |  |  |
| 5 | `DTSTARTTIME` | TIME |  |  |  |  |
| 6 | `DTENDDATE` | DATE |  |  |  |  |
| 7 | `DTENDDATEUTC` | TIMESTAMP |  |  |  |  |
| 8 | `DTENDTIME` | TIME |  |  |  |  |
| 9 | `FULLDAYEVENT` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ZONEID` | CHAR(35) |  |  |  |  |
| 11 | `LOCATION` | VARCHAR(150) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `RELATEDABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSMAILBOX_ATTEVENT` | `ABSMAILBOXMAILIDENTIFIER` | [`ABSMAILBOX`](../PLATFORM/ABSMAILBOX.md) | `MAILIDENTIFIER` | RESTRICT | `ABSMAILBOXVEVENT.ABSMAILBOXMAILIDENTIFIER = ABSMAILBOX.MAILIDENTIFIER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ABSMAILBOXVEVENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ABSMAILBOXMAILIDENTIFIER,
       t.PROPKEY,
       t.ORGANIZERASCHAIR,
       t.DTSTARTDATE,
       t.DTSTARTDATEUTC,
       t.DTSTARTTIME,
       t.DTENDDATE,
       t.DTENDDATEUTC,
       t.DTENDTIME,
       t.FULLDAYEVENT,
       t.ZONEID,
       t.LOCATION
FROM   DB2ADMIN.ABSMAILBOXVEVENT t
FETCH FIRST 100 ROWS ONLY;
```
