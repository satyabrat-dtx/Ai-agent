# DB2ADMIN.CSRMSCHEDULE

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `UNIQUEID`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118577

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  | FK | foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DOCUMENTNUMBER` | CHAR(20) |  |  |  |  |
| 2 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `ZONEID` | CHAR(35) |  |  |  |  |
| 5 | `PLANNEDSTARTDATE` | DATE | NOT NULL |  |  |  |
| 6 | `PLANNEDENDDATE` | DATE | NOT NULL |  |  |  |
| 7 | `PLANNEDSTARTTIME` | TIME |  |  |  |  |
| 8 | `PLANNEDENDTIME` | TIME |  |  |  |  |
| 9 | `ACTUALSTARTDATE` | DATE |  |  |  |  |
| 10 | `ACTUALENDDATE` | DATE |  |  |  |  |
| 11 | `ACTUALSTARTTIME` | TIME |  |  |  |  |
| 12 | `ACTUALENDTIME` | TIME |  |  |  |  |
| 13 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 14 | `CALENDARCOLOR` | CHAR(16) |  |  |  |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `BODY` | VARCHAR(1000) |  |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 27 | `USERIDUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 28 | `EMAIL` | CHAR(150) |  |  |  |  |
| 29 | `FROMPARTICIPANT` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_USERID` | `USERIDUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `CSRMSCHEDULE.USERIDUSERID = ABSUSERDEF.USERID` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CSRMSCHEDULE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CSRMSCHEDULEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DOCUMENTNUMBER,
       t.UNIQUEID,
       t.CODE,
       t.ZONEID,
       t.PLANNEDSTARTDATE,
       t.PLANNEDENDDATE,
       t.PLANNEDSTARTTIME,
       t.PLANNEDENDTIME,
       t.ACTUALSTARTDATE,
       t.ACTUALENDDATE,
       t.ACTUALSTARTTIME
FROM   DB2ADMIN.CSRMSCHEDULE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
