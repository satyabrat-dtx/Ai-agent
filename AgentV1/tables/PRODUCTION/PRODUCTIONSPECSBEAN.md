# DB2ADMIN.PRODUCTIONSPECSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `staging_mirror`
- **Columns**: 44
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 96554

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `INITIALDATE` | DATE |  |  |  |  |
| 3 | `FINALDATE` | DATE |  |  |  |  |
| 4 | `TEMPLATECODE` | CHAR(8) |  |  |  |  |
| 5 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 6 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 7 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 8 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 10 | `WRKCTRANDOPERATTRCODE` | CHAR(20) |  |  |  |  |
| 11 | `RESOURCEGROUPCODE` | CHAR(5) |  |  |  |  |
| 12 | `RESOURCECODE` | CHAR(8) |  |  |  |  |
| 13 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 14 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 15 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 22 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 23 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `USERGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 25 | `USERGROUPCODE` | CHAR(10) |  |  |  |  |
| 26 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 27 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 28 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 29 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 30 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 31 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 32 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 33 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 34 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 35 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 36 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 37 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 38 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 39 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 40 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 41 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 42 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 43 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PRODUCTIONSPECSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.IMPORTAUTOCOUNTER,
       t.INITIALDATE,
       t.FINALDATE,
       t.TEMPLATECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.WRKCTRANDOPERATTRCODE,
       t.RESOURCEGROUPCODE
FROM   DB2ADMIN.PRODUCTIONSPECSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
