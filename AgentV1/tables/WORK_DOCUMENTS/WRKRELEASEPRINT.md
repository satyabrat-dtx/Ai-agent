# DB2ADMIN.WRKRELEASEPRINT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 78
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31415

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `RELEASECODE` | CHAR(15) |  |  |  |  |
| 5 | `RELEASELINE` | DECIMAL(7,0) |  |  |  |  |
| 6 | `RELEASESUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 7 | `RELEASECOMPONENTRELEASELINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `LANGUAGECODE` | CHAR(2) |  |  |  |  |
| 9 | `CHOICEDELIVERYPOINT` | CHAR(2) |  |  |  |  |
| 10 | `DELIVERYPOINTLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 11 | `DELIVERYPOINTLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 12 | `DELIVERYPOINTADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 13 | `DELIVERYPOINTADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 14 | `DELIVERYPOINTADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 15 | `DELIVERYPOINTPOSTALCODE` | CHAR(20) |  |  |  |  |
| 16 | `DELIVERYPOINTTOWN` | VARCHAR(200) |  |  |  |  |
| 17 | `DELIVERYPOINTDISTRICT` | VARCHAR(200) |  |  |  |  |
| 18 | `DELIVERYPOINTCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 19 | `DELIVERYCNYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 20 | `CHOICEDOCUMENTADDRESS` | CHAR(2) |  |  |  |  |
| 21 | `DOCUMENTADDRESSLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 22 | `DOCUMENTADDRESSLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 23 | `DOCUMENTADDRESSADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 24 | `DOCUMENTADDRESSADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 25 | `DOCUMENTADDRESSADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 26 | `DOCUMENTADDRESSPOSTALCODE` | CHAR(20) |  |  |  |  |
| 27 | `DOCUMENTADDRESSTOWN` | VARCHAR(200) |  |  |  |  |
| 28 | `DOCUMENTADDRESSDISTRICT` | VARCHAR(200) |  |  |  |  |
| 29 | `DOCUMENTADDRESSCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 30 | `DOCADDRESSCNYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 31 | `DOCUMENTADDRESSFISCALCODE` | CHAR(16) |  |  |  |  |
| 32 | `CHOICESHIPPINGADDRESS` | CHAR(2) |  |  |  |  |
| 33 | `FINANCIALADDRESSLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 34 | `FINANCIALADDRESSLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 35 | `FINANCIALADDRESSADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 36 | `FINANCIALADDRESSADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 37 | `FINANCIALADDRESSADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 38 | `FINANCIALADDRESSPOSTALCODE` | CHAR(20) |  |  |  |  |
| 39 | `FINANCIALADDRESSTOWN` | VARCHAR(200) |  |  |  |  |
| 40 | `FINANCIALADDRESSDISTRICT` | VARCHAR(200) |  |  |  |  |
| 41 | `FINANCIALADDRESSCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 42 | `FNCADDRESSCNYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 43 | `FINANCIALADDRESSFISCALCODE` | CHAR(16) |  |  |  |  |
| 44 | `PAYMENTADDRESSLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 45 | `PAYMENTADDRESSLEGALNAME2` | VARCHAR(200) |  |  |  |  |
| 46 | `PAYMENTADDRESSADDRESSLINE1` | VARCHAR(200) |  |  |  |  |
| 47 | `PAYMENTADDRESSADDRESSLINE2` | VARCHAR(200) |  |  |  |  |
| 48 | `PAYMENTADDRESSADDRESSLINE3` | VARCHAR(200) |  |  |  |  |
| 49 | `PAYMENTADDRESSPOSTALCODE` | CHAR(20) |  |  |  |  |
| 50 | `PAYMENTADDRESSTOWN` | VARCHAR(200) |  |  |  |  |
| 51 | `PAYMENTADDRESSDISTRICT` | VARCHAR(200) |  |  |  |  |
| 52 | `PAYMENTADDRESSCOUNTRYCODE` | CHAR(3) |  |  |  |  |
| 53 | `PAYADDRESSCNYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 54 | `COMPANYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 55 | `DIVISIONLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 56 | `STCGROUPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 57 | `PROJECTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 58 | `TERMSOFDLVLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 59 | `TERMSOFSHPLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 60 | `TRANSPORTREALONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 61 | `AREALONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 62 | `FIRSTCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 63 | `SECONDCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 64 | `THIRDCARRIERLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 65 | `ORDERCATEGORYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 66 | `CURRENCYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 67 | `PAYMENTMETHODLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 68 | `PRICELISTLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 69 | `DSCCATEGORYLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 70 | `TAXLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 71 | `BANKLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 72 | `BANKEXTERNALLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 73 | `AGENT1LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 74 | `AGENT2LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 75 | `AGENT3LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 76 | `AGENT4LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 77 | `AGENT5LONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.RELEASECODE,
       t.RELEASELINE,
       t.RELEASESUBLINE,
       t.RELEASECOMPONENTRELEASELINE,
       t.LANGUAGECODE,
       t.CHOICEDELIVERYPOINT,
       t.DELIVERYPOINTLEGALNAME1,
       t.DELIVERYPOINTLEGALNAME2
FROM   DB2ADMIN.WRKRELEASEPRINT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
