# DB2ADMIN.PRODUCTIONORDERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `staging_mirror`
- **Columns**: 59
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 87786

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PREVIOUSALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 1 | `PREVIOUSDEMANDLIST` | CLOB(24000) |  |  |  |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 4 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 5 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 6 | `PRODUCTIONORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 7 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `DEMANDLIST` | CLOB(24000) |  |  |  |  |
| 9 | `ENTRY` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ISSUE` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ORDERDATE` | DATE |  |  |  |  |
| 12 | `STATUS` | CHAR(2) |  |  |  |  |
| 13 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 14 | `AUTOMATICCREATIONDEMAND` | SMALLINT | NOT NULL |  |  |  |
| 15 | `HANDLEDYELOTUOM` | SMALLINT | NOT NULL |  |  |  |
| 16 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 17 | `STDPRODUCTIONBATCHUOMCODE` | CHAR(3) |  |  |  |  |
| 18 | `TOTALPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 19 | `PRIMARYUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 20 | `NEWTOTALPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `TOTALSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `SECONDARYUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 23 | `TOTALPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `PACKAGINGUNITOFMEASURECODE` | CHAR(3) |  |  |  |  |
| 25 | `NEWORDERDATE` | DATE |  |  |  |  |
| 26 | `NEWTOTALSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 27 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 28 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 29 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 30 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 31 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 35 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 36 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 37 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 38 | `BASEPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 39 | `BASEPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `BASESECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 41 | `BASESECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 42 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 43 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 44 | `FORCEDELETE` | SMALLINT | NOT NULL |  |  |  |
| 45 | `TNAHEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 46 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 47 | `ACTIVITYDATE` | TIMESTAMP |  |  |  |  |
| 48 | `TNASTARTDATE` | TIMESTAMP |  |  |  |  |
| 49 | `TNAENDDATE` | TIMESTAMP |  |  |  |  |
| 50 | `TNARECALCULATIONENDDATE` | TIMESTAMP |  |  |  |  |
| 51 | `TNASTATUS` | INTEGER | NOT NULL |  |  |  |
| 52 | `REALIGNTNA` | SMALLINT | NOT NULL |  |  |  |
| 53 | `GANTTMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 54 | `TNAGANTTRESOURCEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 55 | `TNAGANTTMARKERREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 56 | `TNAGANTTLINKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 57 | `TNAGANTTSUBTASKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 58 | `TNAACTIVITYGANTT` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIONORDERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.PREVIOUSALLOWEDDIVISIONS,
       t.PREVIOUSDEMANDLIST,
       t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.PRODUCTIONORDERCOUNTERCODE,
       t.CODE,
       t.DEMANDLIST,
       t.ENTRY,
       t.ISSUE,
       t.ORDERDATE
FROM   DB2ADMIN.PRODUCTIONORDERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
