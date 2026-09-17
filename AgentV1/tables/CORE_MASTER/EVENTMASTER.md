# DB2ADMIN.EVENTMASTER

- **Module**: `CORE_MASTER` (low confidence — referenced across 4 modules, so shared reference data)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `CODE`
- **FK degree**: referenced by 11 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 121621

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 1 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 2 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 3 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 4 | `WSDLNAME` | VARCHAR(200) | NOT NULL |  |  |  |
| 5 | `DOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 6 | `PURCHASEDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 7 | `DEBITDOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 8 | `USERNAME` | CHAR(20) | NOT NULL |  |  |  |
| 9 | `PASSWORD` | CHAR(15) |  |  |  |  |
| 10 | `WSDLURL` | LONG VARCHAR | NOT NULL |  |  |  |
| 11 | `BATCHWSDLURL` | LONG VARCHAR | NOT NULL |  |  |  |
| 12 | `OPERATIONNAME` | CHAR(50) |  |  |  |  |
| 13 | `WSDLQNAMEURL` | CHAR(50) | NOT NULL |  |  |  |
| 14 | `WSDLREQUESTNAME` | CHAR(50) | NOT NULL |  |  |  |
| 15 | `WSDLREQUESTTYPE` | CHAR(50) | NOT NULL |  |  |  |
| 16 | `WSDLRESPONSENAME` | CHAR(50) | NOT NULL |  |  |  |
| 17 | `WSDLRESPONSETYPE` | CHAR(50) | NOT NULL |  |  |  |
| 18 | `SOAPACTION` | CHAR(50) | NOT NULL |  |  |  |
| 19 | `ACTIVATESERVICE` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 21 | `PRODUCTIONCOST` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 11

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `EVENTMASTER_EVENT` | [`BUSINESSAREAVSCOSTCENTER`](../COSTING/BUSINESSAREAVSCOSTCENTER.md) | `EVENTCODE` | `BUSINESSAREAVSCOSTCENTER.EVENTCODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENT` | [`EVENTVSBENEFITGLMAPPING`](../OTHER/EVENTVSBENEFITGLMAPPING.md) | `EVENTCODE` | `EVENTVSBENEFITGLMAPPING.EVENTCODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENT` | [`EVENTVSTAXCODEVSGL`](../OTHER/EVENTVSTAXCODEVSGL.md) | `EVENTCODE` | `EVENTVSTAXCODEVSGL.EVENTCODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENT` | [`CSMINTERFACECONTROL`](../OTHER/CSMINTERFACECONTROL.md) | `EVENTCODE` | `CSMINTERFACECONTROL.EVENTCODE = EVENTMASTER.CODE` |
| `EVENTMASTER_POSTINGTYPE` | [`RG23SAPERRORINTERFACE`](../OTHER/RG23SAPERRORINTERFACE.md) | `POSTINGTYPECODE` | `RG23SAPERRORINTERFACE.POSTINGTYPECODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENTCODE` | [`RG23TAXVSGLCODE`](../OTHER/RG23TAXVSGLCODE.md) | `EVENTCODECODE` | `RG23TAXVSGLCODE.EVENTCODECODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENT` | [`PAYELEMVSEVENTGLMAP`](../OTHER/PAYELEMVSEVENTGLMAP.md) | `EVENTCODE` | `PAYELEMVSEVENTGLMAP.EVENTCODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENT` | [`FINEVENTCOSTCENTERMAP`](../FINANCE/FINEVENTCOSTCENTERMAP.md) | `EVENTCODE` | `FINEVENTCOSTCENTERMAP.EVENTCODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENT` | [`NETFINTRANSACTIONHEADER`](../LOCALIZATION/NETFINTRANSACTIONHEADER.md) | `EVENTCODE` | `NETFINTRANSACTIONHEADER.EVENTCODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENT` | [`PERIODCOSTHEADER`](../OTHER/PERIODCOSTHEADER.md) | `EVENTCODE` | `PERIODCOSTHEADER.EVENTCODE = EVENTMASTER.CODE` |
| `EVENTMASTER_EVENT` | [`ITEMVSEVENTGLMAP`](../ITEM_MASTER/ITEMVSEVENTGLMAP.md) | `EVENTCODE` | `ITEMVSEVENTGLMAP.EVENTCODE = EVENTMASTER.CODE` |

## Indexes

- `EVENTMASTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.WSDLNAME,
       t.DOCUMENTTYPE,
       t.PURCHASEDOCUMENTTYPE,
       t.DEBITDOCUMENTTYPE,
       t.USERNAME,
       t.PASSWORD,
       t.WSDLURL,
       t.BATCHWSDLURL
FROM   DB2ADMIN.EVENTMASTER t
FETCH FIRST 100 ROWS ONLY;
```
