# DB2ADMIN.WORKCENTERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `staging_mirror`
- **Columns**: 65
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 62578

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 8 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 9 | `RESPONSIBLECODE` | CHAR(50) |  |  |  |  |
| 10 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 11 | `CALENDARCODE` | CHAR(3) |  |  |  |  |
| 12 | `PERIODIZEDCALENDARTYPECODE` | CHAR(10) |  |  |  |  |
| 13 | `WAREHOUSEWIPCODE` | CHAR(8) |  |  |  |  |
| 14 | `LOCWIPISSUEWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 15 | `LOCWIPISSUEWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 16 | `LOCATIONWIPISSUECODE` | CHAR(10) |  |  |  |  |
| 17 | `LOCWIPENTRYWHSZONEPHYWHSCODE` | CHAR(8) |  |  |  |  |
| 18 | `LOCWIPENTRYWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 19 | `LOCATIONWIPENTRYCODE` | CHAR(10) |  |  |  |  |
| 20 | `TYPE` | CHAR(2) |  |  |  |  |
| 21 | `SUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 22 | `SUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 23 | `NUMBEROFMAINRESOURCES` | DECIMAL(3,0) |  |  |  |  |
| 24 | `NRRESOURCEDETAIL` | DECIMAL(3,0) |  |  |  |  |
| 25 | `QUEUETIMEONENTRANCE` | DECIMAL(10,5) |  |  |  |  |
| 26 | `QUEUETIMEUNIT` | CHAR(2) |  |  |  |  |
| 27 | `STANDARDEFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 28 | `STANDARDEFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 29 | `CRITICALRESOURCECODE` | CHAR(8) |  |  |  |  |
| 30 | `WORKCENTERGROUPCODE` | CHAR(3) |  |  |  |  |
| 31 | `BATHVOLUME` | DECIMAL(17,6) |  |  |  |  |
| 32 | `BATHVOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 33 | `TEMPERATURELOSSOVERTIME` | DECIMAL(17,6) |  |  |  |  |
| 34 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 35 | `ADDRESSLINE1` | VARCHAR(150) |  |  |  |  |
| 36 | `ADDRESSLINE2` | VARCHAR(150) |  |  |  |  |
| 37 | `ADDRESSLINE3` | VARCHAR(150) |  |  |  |  |
| 38 | `ADDRESSLINE4` | VARCHAR(150) |  |  |  |  |
| 39 | `ADDRESSLINE5` | VARCHAR(150) |  |  |  |  |
| 40 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 41 | `TOWN` | VARCHAR(200) |  |  |  |  |
| 42 | `DISTRICT` | VARCHAR(200) |  |  |  |  |
| 43 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 44 | `ADDRESSPHONENUMBER` | VARCHAR(80) |  |  |  |  |
| 45 | `ADDRESSFAXNUMBER` | VARCHAR(80) |  |  |  |  |
| 46 | `ALLOWEDDIVISIONSSTR` | VARCHAR(100) |  |  |  |  |
| 47 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 48 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 49 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 50 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 51 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 52 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 53 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 54 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 55 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 56 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 57 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 58 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 59 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 60 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 61 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 62 | `RECLCSTEPTIMEFROMPARTPRG` | SMALLINT | NOT NULL |  |  |  |
| 63 | `EXCLUDEDAILYCAPACITYCREATION` | SMALLINT | NOT NULL |  |  |  |
| 64 | `EXCLUDECHECKOVERCAPACITY` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WORKCENTERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DEPARTMENTCODE,
       t.PLANTCODE,
       t.RESPONSIBLECODE,
       t.COSTCENTERCODE,
       t.CALENDARCODE
FROM   DB2ADMIN.WORKCENTERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
