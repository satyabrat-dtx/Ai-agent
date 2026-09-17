# DB2ADMIN.ABSREPORTDEF

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `CODE`
- **FK degree**: referenced by 5 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 70474

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(50) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `NAME` | CHAR(50) | NOT NULL |  |  |  |
| 2 | `DESCRIPTION` | VARCHAR(250) | NOT NULL |  | description |  |
| 3 | `PACKAGE` | CHAR(50) |  |  |  |  |
| 4 | `PREPARECLASSNAME` | CHAR(50) |  |  |  |  |
| 5 | `POSTCLASSNAME` | CHAR(50) |  |  |  |  |
| 6 | `RESOURCEBUNDLE` | CHAR(50) |  |  |  |  |
| 7 | `CONNECTIONNAME` | CHAR(100) |  |  |  |  |
| 8 | `USERDESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 9 | `OUTPUTTYPE` | INTEGER | NOT NULL |  |  |  |
| 10 | `OUTPUTFORMAT` | INTEGER | NOT NULL |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `LOGICALREPORT` | SMALLINT | NOT NULL |  |  |  |
| 16 | `REALREPORTCODE` | CHAR(50) |  | FK | foreign_key |  |
| 17 | `NRCOPIES` | INTEGER | NOT NULL |  |  |  |
| 18 | `FIXEDPARAMETERFIELDS` | VARCHAR(250) |  |  |  |  |
| 19 | `USERDATAPROPERTIES` | VARCHAR(250) |  |  |  |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `DOWNLOADFILENAME` | CHAR(50) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSREPORTDEF_REALREPORT` | `REALREPORTCODE` | [`ABSREPORTDEF`](../PLATFORM/ABSREPORTDEF.md) | `CODE` | RESTRICT | `ABSREPORTDEF.REALREPORTCODE = ABSREPORTDEF.CODE` |

## Referenced by (child → this table) — 5

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSREPORTDEF_REPORT` | [`ABSUIXMLREPORT`](../PLATFORM/ABSUIXMLREPORT.md) | `REPORTCODE` | `ABSUIXMLREPORT.REPORTCODE = ABSREPORTDEF.CODE` |
| `ABSREPORTDEF_CUSTOMVALUE` | [`ABSREPORTDEFCUSTOMVALUE`](../PLATFORM/ABSREPORTDEFCUSTOMVALUE.md) | `ABSREPORTDEFCODE` | `ABSREPORTDEFCUSTOMVALUE.ABSREPORTDEFCODE = ABSREPORTDEF.CODE` |
| `ABSREPORTDEF_AUTHORIZATIONS` | [`ABSREPORTDEFAUTH`](../PLATFORM/ABSREPORTDEFAUTH.md) | `ABSREPORTDEFCODE` | `ABSREPORTDEFAUTH.ABSREPORTDEFCODE = ABSREPORTDEF.CODE` |
| `ABSREPORTDEF_REALREPORT` | [`ABSREPORTDEF`](../PLATFORM/ABSREPORTDEF.md) | `REALREPORTCODE` | `ABSREPORTDEF.REALREPORTCODE = ABSREPORTDEF.CODE` |
| `ABSREPORTDEF_SUBREPORTS` | [`ABSREPORTDEFSUBREPORTS`](../PLATFORM/ABSREPORTDEFSUBREPORTS.md) | `ABSREPORTDEFCODE` | `ABSREPORTDEFSUBREPORTS.ABSREPORTDEFCODE = ABSREPORTDEF.CODE` |

## Indexes

- `ABSREPORTDEFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.NAME,
       t.DESCRIPTION,
       t.PACKAGE,
       t.PREPARECLASSNAME,
       t.POSTCLASSNAME,
       t.RESOURCEBUNDLE,
       t.CONNECTIONNAME,
       t.USERDESCRIPTION,
       t.OUTPUTTYPE,
       t.OUTPUTFORMAT,
       t.CREATIONDATETIME
FROM   DB2ADMIN.ABSREPORTDEF t
FETCH FIRST 100 ROWS ONLY;
```
