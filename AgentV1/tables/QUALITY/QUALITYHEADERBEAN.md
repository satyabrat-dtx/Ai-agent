# DB2ADMIN.QUALITYHEADERBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `staging_mirror`
- **Columns**: 67
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 120904

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `CODE` | CHAR(20) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `SUBGROUPCODE` | CHAR(5) |  |  |  |  |
| 4 | `NUMBERID` | INTEGER | NOT NULL |  |  |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `DETAILREQUIRED` | CHAR(2) |  |  |  |  |
| 9 | `ORDERPARTNERREQUIRED` | CHAR(1) |  |  |  |  |
| 10 | `TEMPLATECODE` | CHAR(5) |  |  |  |  |
| 11 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 12 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `ITEMDESCRIPTION` | CHAR(200) |  |  |  |  |
| 23 | `QAITEMGROUPCODE` | CHAR(10) |  |  |  |  |
| 24 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 25 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 26 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 27 | `INTERNALSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 28 | `ISOSPECIFICATIONCODE` | CHAR(10) |  |  |  |  |
| 29 | `ADNAMEFORTESTRESULT` | CHAR(50) |  |  |  |  |
| 30 | `QASTATUSCODE` | CHAR(20) |  |  |  |  |
| 31 | `NRTEST` | INTEGER | NOT NULL |  |  |  |
| 32 | `NROFRETRYIFFAILED` | INTEGER | NOT NULL |  |  |  |
| 33 | `SAMPLE` | SMALLINT | NOT NULL |  |  |  |
| 34 | `SAMPLEINSTRUCTIONCODE` | CHAR(3) |  |  |  |  |
| 35 | `SAMPLELENGTH` | DECIMAL(10,5) |  |  |  |  |
| 36 | `PRECREATEREPETITIONLINES` | SMALLINT | NOT NULL |  |  |  |
| 37 | `CALLQCVERIFY` | SMALLINT | NOT NULL |  |  |  |
| 38 | `QCVERIFY` | CHAR(1) |  |  |  |  |
| 39 | `FREQUENCYCHECK` | SMALLINT | NOT NULL |  |  |  |
| 40 | `FREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 41 | `QUANTITYCHECK` | SMALLINT | NOT NULL |  |  |  |
| 42 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 43 | `OCCURRENCESCHECK` | SMALLINT | NOT NULL |  |  |  |
| 44 | `OCCURRENCES` | INTEGER | NOT NULL |  |  |  |
| 45 | `ENTITYKEYVECTOR` | VARCHAR(2000) |  |  |  |  |
| 46 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 47 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
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
| 58 | `STATUSINACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 59 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 60 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 61 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 62 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 63 | `RETRYONLYFORFAILEDLINES` | SMALLINT | NOT NULL |  |  |  |
| 64 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 65 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 66 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUALITYHEADERBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.CODE,
       t.SUBGROUPCODE,
       t.NUMBERID,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DETAILREQUIRED,
       t.ORDERPARTNERREQUIRED,
       t.TEMPLATECODE,
       t.ITEMTYPEAFICODE
FROM   DB2ADMIN.QUALITYHEADERBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
