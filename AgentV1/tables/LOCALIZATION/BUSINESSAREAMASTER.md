# DB2ADMIN.BUSINESSAREAMASTER

- **Module**: `LOCALIZATION` (low confidence — FK neighbourhood: 1 of 1 related tables are LOCALIZATION)
- **Roles**: `business_data`
- **Columns**: 5
- **Primary key**: `CODE`
- **FK degree**: referenced by 4 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121307

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(50) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BUSINESSAREAMASTER_BUSINESSAREA` | [`BUSINESSAREAVSCOMPANY`](../LOCALIZATION/BUSINESSAREAVSCOMPANY.md) | `BUSINESSAREACODE` | `BUSINESSAREAVSCOMPANY.BUSINESSAREACODE = BUSINESSAREAMASTER.CODE` |
| `BUSINESSAREAMASTER_BUSUNT` | [`BUSINESSGRPVSBUNIT`](../OTHER/BUSINESSGRPVSBUNIT.md) | `BUSUNTCODE` | `BUSINESSGRPVSBUNIT.BUSUNTCODE = BUSINESSAREAMASTER.CODE` |
| `BUSINESSAREAMASTER_BUSINESSAREA` | [`NETFINTRANSACTIONHEADER`](../LOCALIZATION/NETFINTRANSACTIONHEADER.md) | `BUSINESSAREACODE` | `NETFINTRANSACTIONHEADER.BUSINESSAREACODE = BUSINESSAREAMASTER.CODE` |
| `BUSINESSAREAMASTER_BUSINESSAREA` | [`PERIODCOSTHEADER`](../OTHER/PERIODCOSTHEADER.md) | `BUSINESSAREACODE` | `PERIODCOSTHEADER.BUSINESSAREACODE = BUSINESSAREAMASTER.CODE` |

## Indexes

- `BUSINESSAREAMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ABSUNIQUEID
FROM   DB2ADMIN.BUSINESSAREAMASTER t
FETCH FIRST 100 ROWS ONLY;
```
