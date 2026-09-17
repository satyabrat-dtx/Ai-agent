# DB2ADMIN.PMPRVMNTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 52
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193614

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 4 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 10 | `EFFECTIVESTARTDATE` | DATE |  |  |  |  |
| 11 | `EFFECTIVEENDDATE` | DATE |  |  |  |  |
| 12 | `SCHEDULINGTYPE` | INTEGER | NOT NULL |  |  |  |
| 13 | `SCHEDULINGINTERVAL` | INTEGER | NOT NULL |  |  |  |
| 14 | `INTERVALUOM` | INTEGER | NOT NULL |  |  |  |
| 15 | `PRODUCTIONQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `PRODUCTIONQTYPERDAY` | DECIMAL(15,5) |  |  |  |  |
| 17 | `PRODUCTIONQTYUOMCODE` | CHAR(3) |  |  |  |  |
| 18 | `NUMBEROFSCHEDULES` | INTEGER | NOT NULL |  |  |  |
| 19 | `SCHEDULEDTILL` | DATE |  |  |  |  |
| 20 | `ACTIVITYGROUPCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 21 | `ACTIVITYGROUPCODE` | CHAR(15) |  |  |  |  |
| 22 | `SELECTEDACTIVITYGROUP` | CHAR(90) |  |  |  |  |
| 23 | `ACTIVITYCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 24 | `ACTIVITYCODE` | CHAR(15) |  |  |  |  |
| 25 | `SELECTEDACTIVITY` | CHAR(90) |  |  |  |  |
| 26 | `MAILREQUIRED` | INTEGER | NOT NULL |  |  |  |
| 27 | `EMAILID` | CHAR(150) |  |  |  |  |
| 28 | `ESTIMATEDDURATION` | DECIMAL(11,2) |  |  |  |  |
| 29 | `DURATIONUOM` | INTEGER | NOT NULL |  |  |  |
| 30 | `REMARKS` | VARCHAR(1000) |  |  |  |  |
| 31 | `RESPONSIBLEOFSCHEDULINGUSERID` | CHAR(50) |  |  |  |  |
| 32 | `DEFAULTASSIGNEDTOUSERID` | CHAR(50) |  |  |  |  |
| 33 | `PMBOMCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 34 | `PMBOMCODE` | CHAR(15) |  |  |  |  |
| 35 | `NEXTDATE` | DATE |  |  |  |  |
| 36 | `LASTDATE` | DATE |  |  |  |  |
| 37 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 38 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 39 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 40 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 41 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 42 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 43 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 44 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 45 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 46 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 47 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 48 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 49 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 50 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 51 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PMPRVMNTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.COUNTERCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.STATUS,
       t.EFFECTIVESTARTDATE,
       t.EFFECTIVEENDDATE
FROM   DB2ADMIN.PMPRVMNTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
