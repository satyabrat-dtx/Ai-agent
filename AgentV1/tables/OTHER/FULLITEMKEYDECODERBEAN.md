# DB2ADMIN.FULLITEMKEYDECODERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 100
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 61959

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONSSTR` | VARCHAR(100) |  |  |  |  |
| 4 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 5 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `IDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 16 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 17 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 18 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 19 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 20 | `EXTERNALCODE` | CHAR(30) |  |  |  |  |
| 21 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 22 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 23 | `OWNINGCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 25 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 26 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 27 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 28 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 29 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 30 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 31 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 32 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 33 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 34 | `SUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 35 | `SUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 36 | `SUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 37 | `SUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 38 | `SUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 39 | `SUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 40 | `SUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 41 | `SUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 42 | `SUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 43 | `SUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 44 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 45 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 46 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 47 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 48 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 49 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 50 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 51 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 52 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 53 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 54 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 55 | `KEEPOLDPRICE` | SMALLINT | NOT NULL |  |  |  |
| 56 | `INTERNALPRICE` | DECIMAL(18,5) |  |  |  |  |
| 57 | `INTERNALPRICEUOMCODE` | CHAR(3) |  |  |  |  |
| 58 | `VALIDFROMDATE` | DATE |  |  |  |  |
| 59 | `VALIDTODATE` | DATE |  |  |  |  |
| 60 | `INTPRICELISTCODE` | CHAR(8) |  |  |  |  |
| 61 | `INTPRICECOSTGROUPCODE` | CHAR(8) |  |  |  |  |
| 62 | `INTPRICEPLANTCODE` | CHAR(8) |  |  |  |  |
| 63 | `NUMBEROFKEYSTOINPUT` | INTEGER | NOT NULL |  |  |  |
| 64 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 65 | `MAXLAYLENGTH` | DECIMAL(8,3) |  |  |  |  |
| 66 | `MAXNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 67 | `WIDTHRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 68 | `WIDTHRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 69 | `GSMRANGEFROM` | DECIMAL(5,2) |  |  |  |  |
| 70 | `GSMRANGETO` | DECIMAL(5,2) |  |  |  |  |
| 71 | `SHRINKAGE` | DECIMAL(5,2) |  |  |  |  |
| 72 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 73 | `ITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 74 | `NOSTATUSMANAGED` | INTEGER | NOT NULL |  |  |  |
| 75 | `ARTICLESTATUSCODE` | CHAR(8) |  |  |  |  |
| 76 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 77 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 78 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 79 | `BARCODEOUTPUT` | CHAR(1) |  |  |  |  |
| 80 | `QRCODE` | CHAR(200) |  |  |  |  |
| 81 | `QRBARCODE` | CHAR(1) |  |  |  |  |
| 82 | `AVOIDROLLBACK` | SMALLINT | NOT NULL |  |  |  |
| 83 | `BARCODECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 84 | `QRCODECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 85 | `TNAHEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `TNAHEADERCODE` | CHAR(10) |  |  |  |  |
| 87 | `ACTIVITYDATE` | TIMESTAMP |  |  |  |  |
| 88 | `TNASTARTDATE` | TIMESTAMP |  |  |  |  |
| 89 | `TNAENDDATE` | TIMESTAMP |  |  |  |  |
| 90 | `TNARECALCULATIONENDDATE` | TIMESTAMP |  |  |  |  |
| 91 | `TNASTATUS` | INTEGER | NOT NULL |  |  |  |
| 92 | `REALIGNTNA` | SMALLINT | NOT NULL |  |  |  |
| 93 | `GANTTMANAGED` | SMALLINT | NOT NULL |  |  |  |
| 94 | `TNAGANTTRESOURCEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 95 | `TNAGANTTMARKERREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 96 | `TNAGANTTLINKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 97 | `TNAGANTTSUBTASKREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 98 | `TNAACTIVITYGANTT` | CLOB(1000000) |  |  |  |  |
| 99 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FULLITEMKEYDECODERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONSSTR,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.FULLITEMKEYDECODERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
