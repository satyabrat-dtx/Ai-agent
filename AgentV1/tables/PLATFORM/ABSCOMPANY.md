# DB2ADMIN.ABSCOMPANY

- **Module**: `PLATFORM` (high confidence — table name starts with 'ABS')
- **Roles**: `business_data`
- **Columns**: 28
- **Primary key**: `CODE`
- **FK degree**: referenced by 9 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34224

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `DESCRIPTION` | VARCHAR(200) | NOT NULL |  | description |  |
| 2 | `LANGUAGECODE` | CHAR(2) |  | FK | foreign_key |  |
| 3 | `COMPANYGROUP` | SMALLINT | NOT NULL |  |  |  |
| 4 | `GROUPCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `MULTIDIVISIONALLOWED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `SENDEREMAIL` | CHAR(150) |  |  |  |  |
| 7 | `SENDERSMTPID` | CHAR(150) |  |  |  |  |
| 8 | `SENDERSMTPPWD` | CHAR(20) |  |  |  |  |
| 9 | `SMTPSERVERADDR` | CHAR(64) |  |  |  |  |
| 10 | `SMTPSERVERPORT` | CHAR(5) |  |  |  |  |
| 11 | `SMTPUSETLS` | INTEGER | NOT NULL |  |  |  |
| 12 | `SMTPUSEAUTH` | INTEGER | NOT NULL |  |  |  |
| 13 | `MAILSIGNATURE` | VARCHAR(250) |  |  |  |  |
| 14 | `NOTIFYOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 15 | `NOTIFYRETURNOPTIONS` | INTEGER | NOT NULL |  |  |  |
| 16 | `RETURNRECEIPT` | INTEGER | NOT NULL |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `TIMEZONEENABLED` | SMALLINT | NOT NULL |  |  |  |
| 23 | `ZONEID` | CHAR(35) |  |  |  |  |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `SMTPUSEUTF8` | INTEGER | NOT NULL |  |  |  |
| 27 | `SMTPCUSTOMPROPS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSAVAILABLELANGUAGE_LANGUAGE` | `LANGUAGECODE` | [`ABSAVAILABLELANGUAGE`](../PLATFORM/ABSAVAILABLELANGUAGE.md) | `CODE` | RESTRICT | `ABSCOMPANY.LANGUAGECODE = ABSAVAILABLELANGUAGE.CODE` |
| `ABSCOMPANY_GROUP` | `GROUPCODE` | [`ABSCOMPANY`](../PLATFORM/ABSCOMPANY.md) | `CODE` | RESTRICT | `ABSCOMPANY.GROUPCODE = ABSCOMPANY.CODE` |

## Referenced by (child → this table) — 9

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ABSCOMPANY_DIVISION` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE` | `DIVISION.COMPANYCODE = ABSCOMPANY.CODE` |
| `ABSCOMPANY_GROUP` | [`ABSCOMPANY`](../PLATFORM/ABSCOMPANY.md) | `GROUPCODE` | `ABSCOMPANY.GROUPCODE = ABSCOMPANY.CODE` |
| `ABSCOMPANY_COMPANY` | [`ABSUSERCOMPANY`](../PLATFORM/ABSUSERCOMPANY.md) | `COMPANYCODE` | `ABSUSERCOMPANY.COMPANYCODE = ABSCOMPANY.CODE` |
| `ABSCOMPANY_ABSCOMPANY` | [`ABSDIVISIONHANDLING`](../PLATFORM/ABSDIVISIONHANDLING.md) | `ABSCOMPANYCODE` | `ABSDIVISIONHANDLING.ABSCOMPANYCODE = ABSCOMPANY.CODE` |
| `ABSCOMPANY_COMPANY` | [`WFMCUSTOMIZEDOPTIONS`](../PLATFORM/WFMCUSTOMIZEDOPTIONS.md) | `COMPANYCODE` | `WFMCUSTOMIZEDOPTIONS.COMPANYCODE = ABSCOMPANY.CODE` |
| `ABSCOMPANY_COMPANY` | [`WFMPROCESS`](../PLATFORM/WFMPROCESS.md) | `COMPANYCODE` | `WFMPROCESS.COMPANYCODE = ABSCOMPANY.CODE` |
| `ABSCOMPANY_COMPANY` | [`SAVEDSTATEMENT`](../PLATFORM/SAVEDSTATEMENT.md) | `COMPANYCODE` | `SAVEDSTATEMENT.COMPANYCODE = ABSCOMPANY.CODE` |
| `ABSCOMPANY_DESTINATIONCOMPANY` | [`ICITEMTYPELEVMAPDEST`](../PLATFORM/ICITEMTYPELEVMAPDEST.md) | `DESTINATIONCOMPANYCODE` | `ICITEMTYPELEVMAPDEST.DESTINATIONCOMPANYCODE = ABSCOMPANY.CODE` |
| `ABSCOMPANY_COMPANY` | [`ABSTAGS`](../PLATFORM/ABSTAGS.md) | `COMPANYCODE` | `ABSTAGS.COMPANYCODE = ABSCOMPANY.CODE` |

## Indexes

- `ABSCOMPANYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.DESCRIPTION,
       t.LANGUAGECODE,
       t.COMPANYGROUP,
       t.GROUPCODE,
       t.MULTIDIVISIONALLOWED,
       t.SENDEREMAIL,
       t.SENDERSMTPID,
       t.SENDERSMTPPWD,
       t.SMTPSERVERADDR,
       t.SMTPSERVERPORT,
       t.SMTPUSETLS
FROM   DB2ADMIN.ABSCOMPANY t
FETCH FIRST 100 ROWS ONLY;
```
