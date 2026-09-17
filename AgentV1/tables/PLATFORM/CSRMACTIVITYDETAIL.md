# DB2ADMIN.CSRMACTIVITYDETAIL

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 29
- **Primary key**: `UNIQUEID`, `ACTIVITYCODE`, `SEQNO`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 118428

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  | FK | foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SEQNO` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 2 | `ACTIVITYCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DOCUMENTNUMBER` | CHAR(20) |  |  |  |  |
| 4 | `REMARKS` | CHAR(50) |  |  |  |  |
| 5 | `STARTDATE` | DATE | NOT NULL |  |  |  |
| 6 | `ACTUALSTARTDATE` | DATE |  |  |  |  |
| 7 | `ENDDATE` | DATE | NOT NULL |  |  |  |
| 8 | `ACTUALENDDATE` | DATE |  |  |  |  |
| 9 | `ACTIVITYBASEDONCODE` | CHAR(15) |  | FK | foreign_key |  |
| 10 | `CALENDARCOLOR` | CHAR(16) |  |  |  |  |
| 11 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 12 | `USERRESPNSBLUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 13 | `MESSAGETYPE` | INTEGER | NOT NULL |  |  |  |
| 14 | `MESSAGETOUSERID` | CHAR(50) |  | FK | foreign_key |  |
| 15 | `MESSAGEWHEN` | CHAR(90) |  |  |  |  |
| 16 | `PARENTENTITY` | INTEGER | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 25 | `BASEDONSTEP` | BIGINT | NOT NULL |  |  |  |
| 26 | `BASEDONTNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 27 | `BASEDONSEQNO` | DECIMAL(5,0) |  |  |  |  |
| 28 | `SCHEDULEMEETING` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_MESSAGETO` | `MESSAGETOUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `CSRMACTIVITYDETAIL.MESSAGETOUSERID = ABSUSERDEF.USERID` |
| `ABSUSERDEF_USERRESPNSBL` | `USERRESPNSBLUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `CSRMACTIVITYDETAIL.USERRESPNSBLUSERID = ABSUSERDEF.USERID` |
| `ACTIVITY_ACTIVITY` | `ACTIVITYCODE` | [`ACTIVITY`](../TNA/ACTIVITY.md) | `CODE` | RESTRICT | `CSRMACTIVITYDETAIL.ACTIVITYCODE = ACTIVITY.CODE` |
| `ACTIVITY_ACTIVITYBASEDON` | `ACTIVITYBASEDONCODE` | [`ACTIVITY`](../TNA/ACTIVITY.md) | `CODE` | RESTRICT | `CSRMACTIVITYDETAIL.ACTIVITYBASEDONCODE = ACTIVITY.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `CSRMACTIVITYDETAIL.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CSRMACTIVITYDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SEQNO,
       t.ACTIVITYCODE,
       t.DOCUMENTNUMBER,
       t.REMARKS,
       t.STARTDATE,
       t.ACTUALSTARTDATE,
       t.ENDDATE,
       t.ACTUALENDDATE,
       t.ACTIVITYBASEDONCODE,
       t.CALENDARCOLOR,
       t.STATUS
FROM   DB2ADMIN.CSRMACTIVITYDETAIL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
