# DB2ADMIN.QUALITYDOCUMENTBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `staging_mirror`
- **Columns**: 61
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 107263

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DETAILREQUIRED` | CHAR(2) |  |  |  |  |
| 3 | `HEADERCODE` | CHAR(20) |  |  |  |  |
| 4 | `HEADERSUBGROUPCODE` | CHAR(5) |  |  |  |  |
| 5 | `HEADERNUMBERID` | INTEGER | NOT NULL |  |  |  |
| 6 | `HEADERDATE` | DATE |  |  |  |  |
| 7 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `LOTCODE` | CHAR(35) |  |  |  |  |
| 19 | `ITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 20 | `ITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 21 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 22 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 23 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 24 | `ORDERPARTNERREQUIRED` | CHAR(1) |  |  |  |  |
| 25 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 26 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 27 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 28 | `STATUS` | CHAR(2) |  |  |  |  |
| 29 | `NOTEINTERNE` | VARCHAR(200) |  |  |  |  |
| 30 | `TESTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 31 | `FULLITEMIDENTIFIER` | DECIMAL(11,0) |  |  |  |  |
| 32 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 33 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 34 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 35 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 36 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 37 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 38 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 39 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 40 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 41 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 42 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 43 | `SAMPLE` | SMALLINT | NOT NULL |  |  |  |
| 44 | `SAMPLEINSTRUCTIONCODE` | CHAR(3) |  |  |  |  |
| 45 | `SAMPLELENGTH` | DECIMAL(10,5) |  |  |  |  |
| 46 | `SAMPLENUMBER` | CHAR(50) |  |  |  |  |
| 47 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 48 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 49 | `HEADERLINE` | DECIMAL(15,0) |  |  |  |  |
| 50 | `PROGRESSSTATUS` | INTEGER | NOT NULL |  |  |  |
| 51 | `EXPORTEDTOPDM` | SMALLINT | NOT NULL |  |  |  |
| 52 | `EXPORTTOPDMVIRTUAL` | SMALLINT | NOT NULL |  |  |  |
| 53 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 54 | `GROUPSTEPNUMBER` | INTEGER | NOT NULL |  |  |  |
| 55 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 56 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 57 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 58 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 59 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 60 | `LOGREASONCODE` | CHAR(2) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUALITYDOCUMENTBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.DETAILREQUIRED,
       t.HEADERCODE,
       t.HEADERSUBGROUPCODE,
       t.HEADERNUMBERID,
       t.HEADERDATE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.QUALITYDOCUMENTBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
