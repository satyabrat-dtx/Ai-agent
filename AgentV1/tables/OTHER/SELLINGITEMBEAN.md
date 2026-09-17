# DB2ADMIN.SELLINGITEMBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `staging_mirror`
- **Columns**: 146
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109092

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 3 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
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
| 15 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 16 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 17 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 18 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 19 | `SUMMARIZEDDESCRIPTION` | CHAR(200) |  |  |  |  |
| 20 | `IMAGENAME` | CHAR(50) |  |  |  |  |
| 21 | `IMAGEPATH` | CHAR(30) |  |  |  |  |
| 22 | `IMAGEVIEW` | CHAR(80) |  |  |  |  |
| 23 | `BARTYPECODE` | CHAR(2) |  |  |  |  |
| 24 | `BARCODE` | VARCHAR(50) |  |  |  |  |
| 25 | `INTERNALITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 26 | `INTERNALSUBCODE01` | CHAR(20) |  |  |  |  |
| 27 | `INTERNALSUBCODE02` | CHAR(10) |  |  |  |  |
| 28 | `INTERNALSUBCODE03` | CHAR(10) |  |  |  |  |
| 29 | `INTERNALSUBCODE04` | CHAR(10) |  |  |  |  |
| 30 | `INTERNALSUBCODE05` | CHAR(10) |  |  |  |  |
| 31 | `INTERNALSUBCODE06` | CHAR(10) |  |  |  |  |
| 32 | `INTERNALSUBCODE07` | CHAR(10) |  |  |  |  |
| 33 | `INTERNALSUBCODE08` | CHAR(10) |  |  |  |  |
| 34 | `INTERNALSUBCODE09` | CHAR(10) |  |  |  |  |
| 35 | `INTERNALSUBCODE10` | CHAR(10) |  |  |  |  |
| 36 | `CATALOGUENUMBER` | INTEGER | NOT NULL |  |  |  |
| 37 | `FREEGIFTTAXDEBIT` | CHAR(1) |  |  |  |  |
| 38 | `TRADEUOMTYPE` | CHAR(2) |  |  |  |  |
| 39 | `TRADEBASEUOMCODE` | CHAR(3) |  |  |  |  |
| 40 | `PRICEUOMTYPE` | CHAR(2) |  |  |  |  |
| 41 | `PRCGRPSTDORDGRPTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 42 | `PRCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 43 | `PRICEGRPCODE` | CHAR(3) |  |  |  |  |
| 44 | `DSCGRPSTDORDGRPTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 45 | `DSCGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 46 | `DISCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 47 | `CHARGEGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 48 | `CHARGEGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 49 | `CHARGEGRPCODE` | CHAR(3) |  |  |  |  |
| 50 | `AGENTGROUPTYPE` | CHAR(1) |  |  |  |  |
| 51 | `AGENTGROUPCODE` | CHAR(3) |  |  |  |  |
| 52 | `AGENTANDCOMMISSIONGRPCODE` | CHAR(3) |  |  |  |  |
| 53 | `BLOCKGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 54 | `BLOCKGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 55 | `BLOCKGRPCODE` | CHAR(3) |  |  |  |  |
| 56 | `ASSORTGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 57 | `ASSORTGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 58 | `ASSORTGRPCODE` | CHAR(3) |  |  |  |  |
| 59 | `EXSGRPSTDORDGRPTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 60 | `EXSGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 61 | `EXCLUSIVEGRPCODE` | CHAR(3) |  |  |  |  |
| 62 | `RESTRICGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 63 | `RESTRICGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 64 | `RESTRICGRPCODE` | CHAR(3) |  |  |  |  |
| 65 | `CMTGRPSTDORDGRPTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 66 | `CMTGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 67 | `COMMENTGRPCODE` | CHAR(3) |  |  |  |  |
| 68 | `TAXGRPSTDORDGRPTYPEORDERTYPE` | CHAR(1) |  |  |  |  |
| 69 | `TAXGRPSTDORDERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 70 | `TAXGRPCODE` | CHAR(3) |  |  |  |  |
| 71 | `MNGACCGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 72 | `MNGACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 73 | `MANAGEMENTACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 74 | `FNCACCGRPSTDORDGRPTYPEORDTYPE` | CHAR(1) |  |  |  |  |
| 75 | `FNCACCGRPSTDORDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 76 | `FINANCIALACCOUNTGRPCODE` | CHAR(3) |  |  |  |  |
| 77 | `FIRSTUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 78 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 79 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 80 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 81 | `THIRDUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 82 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 83 | `FOURTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 84 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 85 | `FIFTHUSERGRPUSERGENGRPTYPECOD` | CHAR(3) |  |  |  |  |
| 86 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 87 | `IDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 88 | `AUTOMATICGENERATION` | SMALLINT | NOT NULL |  |  |  |
| 89 | `ITEMUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 90 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 91 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 92 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 93 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 94 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 95 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 96 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 97 | `DIRTYFIELD` | CHAR(20) |  |  |  |  |
| 98 | `ORDERSUBCODE01` | CHAR(20) |  |  |  |  |
| 99 | `ORDERSUBCODE02` | CHAR(10) |  |  |  |  |
| 100 | `ORDERSUBCODE03` | CHAR(10) |  |  |  |  |
| 101 | `ORDERSUBCODE04` | CHAR(10) |  |  |  |  |
| 102 | `ORDERSUBCODE05` | CHAR(10) |  |  |  |  |
| 103 | `ORDERSUBCODE06` | CHAR(10) |  |  |  |  |
| 104 | `ORDERSUBCODE07` | CHAR(10) |  |  |  |  |
| 105 | `ORDERSUBCODE08` | CHAR(10) |  |  |  |  |
| 106 | `ORDERSUBCODE09` | CHAR(10) |  |  |  |  |
| 107 | `ORDERSUBCODE10` | CHAR(10) |  |  |  |  |
| 108 | `SUBCODE01DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 109 | `SUBCODE02DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 110 | `SUBCODE03DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 111 | `SUBCODE04DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 112 | `SUBCODE05DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 113 | `SUBCODE06DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 114 | `SUBCODE07DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 115 | `SUBCODE08DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 116 | `SUBCODE09DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 117 | `SUBCODE10DESCRIPTION` | VARCHAR(120) |  |  |  |  |
| 118 | `ORDERITEMCODE` | VARCHAR(120) |  |  |  |  |
| 119 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 120 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 121 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 122 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 123 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 124 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 125 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 126 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 127 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 128 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 129 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 130 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 131 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 132 | `CREATIONDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 133 | `CREATIONDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 134 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 135 | `LASTUPDATEDATETIMECMPDIV` | TIMESTAMP |  |  |  |  |
| 136 | `LASTUPDATEDATETIMEUSER` | TIMESTAMP |  |  |  |  |
| 137 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 138 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 139 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 140 | `BARCODEOUTPUT` | CHAR(1) |  |  |  |  |
| 141 | `QRCODE` | CHAR(200) |  |  |  |  |
| 142 | `QRBARCODE` | CHAR(1) |  |  |  |  |
| 143 | `PROTOTYPEMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 144 | `BARCODECHANGED` | SMALLINT | NOT NULL |  |  |  |
| 145 | `QRCODECHANGED` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SELLINGITEMBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.SELLINGITEMBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
